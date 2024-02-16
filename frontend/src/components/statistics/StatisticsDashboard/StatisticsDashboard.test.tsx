import '@testing-library/jest-dom'
import { render, screen } from '@testing-library/react'
import StatisticsDashboard from '../StatisticsDashboard'
import Providers from '@/components/Providers'

describe('StatisticsDashboard', () => {
  test('renders tabs with correct labels and icons', () => {
    render(
      <Providers>
        <StatisticsDashboard />
      </Providers>,
    )

    // Check if all tabs are rendered with correct labels and icons
    expect(screen.getByTestId('tab-all')).toBeInTheDocument()
    expect(screen.getByTestId('tab-players')).toBeInTheDocument()
    expect(screen.getByTestId('tab-teams')).toBeInTheDocument()
  })
})
