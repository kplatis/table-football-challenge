import '@testing-library/jest-dom'
import { render, screen, fireEvent } from '@testing-library/react'
import { Header } from '../Header'
import Providers from '@/components/Providers'

describe('Header', () => {
  test('renders header with menu items', () => {
    render(
      <Providers>
        <Header />
      </Providers>,
    )

    // Check if logo is rendered
    expect(screen.getByText('Challenge')).toBeInTheDocument()

    // Check if menu items are rendered
    expect(screen.getByText('Dashboard')).toBeInTheDocument()
    expect(screen.getByText('Teams')).toBeInTheDocument()
    expect(screen.getByText('Games')).toBeInTheDocument()
  })

  test('toggles menu dropdown when hovering over menu items', async () => {
    render(
      <Providers>
        <Header />
      </Providers>,
    )

    // Open menu dropdown on hover
    fireEvent.mouseEnter(screen.getByText('Teams'))
    expect(await screen.findByText('List teams')).toBeInTheDocument()
  })
})
