import '@testing-library/jest-dom'

import { render, screen } from '@testing-library/react'
import TeamComparison from '../TeamComparison'
import Providers from '@/components/Providers'
import { mockTeams } from '@/__tests__/mockData/teams'

// Mock useTeams hook
jest.mock('@/hooks/useTeams')

describe('TeamComparison', () => {
  test('renders loader when teams are loading', () => {
    // Mock isLoading as true
    jest
      .spyOn(require('@/hooks/useTeams'), 'default')
      .mockImplementation(() => ({
        isLoading: true,
        data: null,
      }))
    render(
      <Providers>
        <TeamComparison />
      </Providers>,
    )

    // Check if loader is rendered
    expect(screen.getByTestId('loader')).toBeInTheDocument()
  })

  test('renders team selection form when teams are loaded', () => {
    // Mock teams data
    jest
      .spyOn(require('@/hooks/useTeams'), 'default')
      .mockImplementation(() => ({
        isLoading: false,
        data: mockTeams,
      }))
    render(
      <Providers>
        <TeamComparison />
      </Providers>,
    )

    // Check if team selection form is rendered
    expect(screen.getByTestId('team-selection-form')).toBeInTheDocument()
  })
})
